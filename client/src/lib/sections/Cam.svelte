<div class="flex flex-col justify-center gap-96">
	<!-- svelte-ignore a11y-media-has-caption -->
	<div class="cam-wrapper2 relative">
		<div class="cam-wrapper grid place-items-center h-[960px] gap-10">
			<div class="video-wrapper rotate-90 overflow-hidden h-[720px] aspect-[4/3]">
				<video class="w-[1000px] block bg-neutral-600 video" bind:this={videoSource} />
			</div>
		</div>
		<div id="count" class="" bind:this={counter}></div>
	</div>

	<div class="flex justify-center anim2">
		<button disabled={started} class="bg-neutral-300 rounded-full w-fit disabled:text-neutral-400 shadow-2xl shadow-black" on:click={capture} style="border: 3px solid green;"
			><IcOutlineCamera class="text-8xl" /></button
		>
	</div>
	<!-- <img bind:this={photo} alt="captured" /> -->
	<!-- <button class="next" on:click={nextSection}>다음으로</button> -->

	<audio id="shutter" bind:this={shutter} src="{`/camera-sound-effects.mp3`}" style="display: hidden;" preload="auto"></audio>
</div>

<style>
.video {
    transform: scale(1.28, .96) translate(110px,-15px);
}
</style>

<script lang="ts">
	import { browser, dev } from '$app/environment'

	import type { Session } from '$lib/stores/sessions'
	import type { Writable } from 'svelte/store'
	import { onMount } from 'svelte'

	import IcOutlineCamera from '$lib/components/icons/IcOutlineCamera.svelte'

	export let session: Writable<Session>

	const width = 960
	let height = 0

	let started = false

	let canvas = null
	let shutter: HTMLAudioElement |null ;
	if (browser) canvas = document.createElement('canvas')
	// let photo = null;
	let wrapper = null
	let wrapperInner = null
	let videoSource = null
	let counter: HTMLElement | null = null
	let loading = false
	const obtenerVideoCamara = async () => {
		loading = true
		const stream = await navigator.mediaDevices.getUserMedia({
			video: { width: { min: 640, max: 640 * 2 }, height: { min: 480, max: 480 * 2 } },
            audio: false
		})
        
		videoSource.srcObject = stream
		videoSource.onloadedmetadata = () => {
			videoSource.play()
			const v = videoSource.getBoundingClientRect()
			height = (videoSource.videoHeight / videoSource.videoWidth) * width
			try {
				wrapper.style.width = `${height}px`
				wrapper.style.height = `${width}px`
				wrapperInner.style.width = `${width}px`
				wrapperInner.style.height = `${height}px`
				videoSource.style.transformOrigin = `${height / 2}px ${height / 2}px`
			} catch (e) {}
			if (!($session.width && $session.height)) {
				$session.width = (videoSource.videoHeight * 4) / 3
				$session.height = videoSource.videoHeight
				//videoSource.style.width =  `100%`
				//videoSource.style.height = `${height}px`
				canvas.width = (videoSource.videoHeight * 4) / 3
				canvas.height = videoSource.videoHeight
			}
		}
		setTimeout(() => {}, 40)
		loading = false
	}

	async function capture() {
		started = true
		// this.classList.add('hidden');
		counter.classList.add('count')

		let i = 0
		
		const intervalId = setInterval(
			async () => {
				counter.innerText = `${10 - (i % 13) > 0 ? 10 - (i % 13) : '✌️'}`
				i++
				videoSource.classList.remove('capture')
				if ((i + 2) % 13) return
				videoSource.classList.add('capture')
				if (i > 3 * 13) {
					clearInterval(intervalId)
					nextSection()
				}
				counter.classList.remove('count')

				shutter.currentTime = 0;
				shutter.play();

				const context = canvas.getContext('2d')
				context.drawImage(videoSource, 0, 0, $session.width, $session.height, 0, 0, $session.width, $session.height)

				const data = canvas.toDataURL('image/png')
				// photo.setAttribute('src', data);

				$session.photos.push(data)

				counter.classList.add('count')
			},
			1 * 100 * (dev ? 1 : 10)
		)

		// let downloadButton = null;
		// if (browser) downloadButton = document.createElement('a');
		// navigator.mediaDevices
		//   .getUserMedia({
		//     video: true,
		//     audio: true,
		//   })
		//   .then((stream) => {
		//     // preview.srcObject = stream;
		//     downloadButton.href = stream;
		//     videoSource.captureStream =
		//       videoSource.captureStream || videoSource.mozCaptureStream;
		//     return new Promise((resolve) => (videoSource.onplaying = resolve));
		//   })
		//   .then(() => startRecording(videoSource.captureStream(), recordingTimeMS))
		//   .then((recordedChunks) => {
		//     let recordedBlob = new Blob(recordedChunks, { type: 'video/webm' });
		//     const result = URL.createObjectURL(recordedBlob);
		//     downloadButton.href = result;
		//     downloadButton.download = 'RecordedVideo.webm';
		//     downloadButton.click();

		//       `Successfully recorded ${recordedBlob.size} bytes of ${recordedBlob.type} media.`,
		//     );
		//   })
		//   .catch((error) => {
		//     if (error.name === 'NotFoundError') {
		//     } else {
		//     }
		//   });
	}

	const nextSection = () => ($session.section += 1)

	// function wait(delayInMS) {
	//   return new Promise((resolve) => setTimeout(resolve, delayInMS));
	// }

	// function stop(stream) {
	//   stream.getTracks().forEach((track) => track.stop());
	// }

	// function startRecording(stream: MediaStream, lengthInMS: number) {
	//   let recorder = new MediaRecorder(stream);
	//   let data = [];

	//   recorder.ondataavailable = (event) => data.push(event.data);
	//   recorder.start();

	//   let stopped = new Promise((resolve, reject) => {
	//     recorder.onstop = resolve;
	//     recorder.onerror = (event) => reject(event.name);
	//   });

	//   let recorded = wait(lengthInMS).then(() => {
	//     if (recorder.state === 'recording') {
	//       recorder.stop();
	//     }
	//   });

	//   return Promise.all([stopped, recorded]).then(() => data);
	// }

	onMount(obtenerVideoCamara)
</script>
