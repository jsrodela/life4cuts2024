<div class="flex flex-col justify-center items-center gap-12">
	<h1 class="text-6xl font-bold font-ridi-serif drop-shadow-[4px_4px_1px_rgba(0,0,0,0.3)]">프레임을 선택해 주세요</h1>

	<div class="flex gap-32">
		{#each [1, 2, 3, 4] as num}
			<button on:click={handleFrameSelection} data-frame={num}>
				<img src={`/frame${num}-preview.webp`} alt="" class="shadow-2xl w-96 border-2 border-neutral-800" />
			</button>
		{/each}
	</div>
</div>

<script lang="ts">
	import type { Session } from '$lib/stores/sessions'
	import type { Writable } from 'svelte/store'

	export let session: Writable<Session>

	function handleFrameSelection(e: MouseEvent & { currentTarget: HTMLElement }) {
		const result = e.currentTarget.getAttribute('data-frame')

		$session.frame = result

		$session.section += 1
	}
</script>
