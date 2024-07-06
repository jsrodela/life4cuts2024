<h1>잠신 네컷</h1>
<p>인원수를 입력하세요</p>

<button class="" on:click={decrement}>-</button>
<span>{`${$session.people}`.padStart(2, '0')} 명</span>
<button on:click={increment}>+</button>

<button on:click={nextSection}>시작하기</button>

<script>
  import { session } from '$lib/stores/sessions';
  import { goto } from '$app/navigation';

  const decrement = () =>
    session.update((s) => {
      if (s.people > 1) s.people -= 1;
      return s;
    });

  const increment = () =>
    session.update((s) => {
      if (s.people < 10) s.people += 1;
      return s;
    });

  const nextSection = () => goto('/cam');
</script>

