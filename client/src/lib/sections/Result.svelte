<div class="flex flex-col gap-48 justify-center items-center">
	<img class="border-2 rotate-90 border-neutral-800 h-[720px] aspect-[4/3]" bind:this={img} alt="" />

	<!-- <img src="/frame1.png" alt="" /> -->
	<!-- <canvas bind:this={canvas}></canvas> -->
	<button
		class="w-fit bg-neutral-200 p-3 h-14 rounded-xl font-ridi-serif font-bold text-4xl flex justify-center items-center hover:bg-neutral-300 transition ease-linear"
		on:click={restartSection}>처음으로</button
	>
</div>

<script lang="ts">
	import { browser } from '$app/environment'
	import { lutImgData } from '$lib/config'

	import { socket, type Session } from '$lib/stores/sessions'
	import { downloadDataUrl } from '$lib/utils/downloadImg'
	import { onMount } from 'svelte'
	import type { Writable } from 'svelte/store'

	export let session: Writable<Session>

	let img = null

	let photoElements: { element: HTMLImageElement; loaded: boolean }[] = []

	function process() {
		if (!browser) return

		console.log('process start')

		const canvas = document.createElement('canvas')

		const imgWidth = $session.width
		const imgHeight = $session.height

		const [paperWidth, paperHeight] = lutImgData[$session.frame].demension

		canvas.width = paperWidth
		canvas.height = paperHeight

		function loadImage() {
			photoElements = Array.from({ length: 4 }, (_, i) => {
				const element = new Image()
				element.src = $session.photos[i]
				const result = {
					element,
					loaded: false,
				}
				element.addEventListener('load', () => {
					result.loaded = true
					console.log(
						`Image ${i} loaded.`,
						`All loaded: `,
						photoElements.every((l) => l.loaded)
					)
					if (photoElements.every((p) => p.loaded)) {
						//photoElements.forEach((element)=>
						//{
						//	console.log(element.src)
						//})
						addImage()
						console.log('image all loaded', $session.width, $session.height)
					}
				})
				return result
			})
		}

		function downloadImages() {
			photoElements.forEach(({ element }) => {
				console.log(element.src)
				const canv = document.createElement('canvas')
				//							canv.width =
			})
		}

		function addImage() {
			photoElements.forEach(({ element }, idx) => {
				const lut = lutImgData[$session.frame]

				console.log(`adding image pos: ${lut.poses[idx][0]} ${lut.poses[idx][1]}`, element)

				canvas.getContext('2d').drawImage(element, lut.poses[idx][0], lut.poses[idx][1], lut.photoWidth, (imgWidth / imgHeight) * lut.photoWidth)

				console.log(lut.poses[idx][0], lut.poses[idx][1], lut.photoWidth, imgHeight, imgWidth, lut.photoWidth)
			})

			applyFrame()
		}

		function applyFrame() {
			let frame = new Image()
			frame.src = `frame${$session.frame}.png`
			//frame.src = '';

			frame.addEventListener('load', () => {
				canvas.getContext('2d').drawImage(frame, 0, 0, paperWidth, paperHeight)

				// const rotatedImg = document.createElement('canvas');

				// rotatedImg.width = paperHeight;
				// rotatedImg.height = paperWidth;

				// const rotatedCtx = rotatedImg.getContext('2d');

				// rotatedCtx.save();
				// rotatedCtx.translate(paperHeight / 2, paperWidth / 2);
				// rotatedCtx.rotate(Math.PI / 2);
				// // rotatedCtx.drawImage(canvas, -paperWidth / 2, -paperHeight / 2);
				// rotatedCtx.restore();

				const data = canvas.toDataURL()

				// img.style.height = `${(paperWidth / paperHeight) * 720}px`;
				// img.style.width = `720px`;

				img.src = data

				img.addEventListener('load', () => {
					console.log('asdas')
					downloadDataUrl(data, `cuts-${$session.people}-${$session.id}`)
					$socket.emit('message', {
						people: $session.people,
						photo: data,
						frame: $session.frame,
					})
				})
			})
		}

		loadImage()
	}

	const restartSection = () => ($session.state = 'end')

	onMount(process)
</script>
