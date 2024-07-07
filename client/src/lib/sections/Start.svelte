<h1>잠신 네컷</h1>
<p>인원수를 입력하세요</p>

<button class="" on:click={decrement}>-</button>
<span>{`${$session.people}`.padStart(2, '0')} 명</span>
<button on:click={increment}>+</button>

<button on:click={nextSection}>시작하기</button>

<script lang="ts">
  import type { Session } from '$lib/stores/sessions';
  import type { Writable } from 'svelte/store';

  export let session: Writable<Session>;

  const decrement = () => $session.people > 1 && ($session.people -= 1);
  const increment = () => $session.people < 10 && ($session.people += 1);

  const nextSection = () => ($session.section += 1);
</script>
