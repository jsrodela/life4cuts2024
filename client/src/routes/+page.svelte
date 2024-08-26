{#if $session.section === 0}
	<Start {session} />
{:else if $session.section === 1}
	<FrameSelect {session} />
{:else if $session.section === 2}
	<Cam {session} />
{:else if $session.section === 3}
	<Result {session} />
{/if}

<script lang="ts">
	import Cam from '$lib/sections/Cam.svelte'
	import Start from '$lib/sections/Start.svelte'
	import Result from '$lib/sections/Result.svelte'
	import FrameSelect from '$lib/sections/FrameSelect.svelte'

	import { newSession, socket } from '$lib/stores/sessions'

	import { dev, browser } from '$app/environment'

	import { io } from 'socket.io-client'

	$socket = io('ws://localhost:4000', {
		reconnectionDelayMax: 10000,
	})

	let session = newSession()

	$: if ($session.state === 'end') session = newSession()

	if (dev && browser) {
		window.addEventListener('keydown', (e) => {
			if (e.key === 'ArrowRight') $session.section += 1
			if (e.key === 'ArrowLeft') $session.section -= 1
		})
	}
</script>
