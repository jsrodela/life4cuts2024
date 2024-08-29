<div class="">
  <div class="grid gap-10 place-items-center">
    <img src={`/neon.png`} width=100 class='anim'/>
    <h1
      class="text-7xl font-bold font-dm-serif drop-shadow-[4px_4px_1px_rgba(0,0,0,0.3)] anim"
    >
      life4cuts
    </h1>

    <p class="text-2xl font-ridi-serif anim1">인원수를 입력하세요</p>

    <div class="flex gap-5 items-center anim2">
      <button
        class="border-2 border-neutral-800 w-14 aspect-square rounded-full font-bold text-4xl flex justify-center leading-tight transition ease-linear disabled:hover:neutral-200 disabled:bg-neutral-200 disabled:text-neutral-500"
        disabled={!($session.people > 1)}
        on:click={decrement}>-</button
      >
      <span
        class="font-bold text-5xl font-dm-serif bg-neutral-200 w-24 aspect-square grid place-items-center rounded-full"
        >{`${$session.people}`}</span
      >
      <button
        class="border-2 border-neutral-800 w-14 aspect-square rounded-full font-bold text-4xl flex justify-center leading-tight transition ease-linear disabled:hover:neutral-200 disabled:bg-neutral-200 disabled:text-neutral-500"
        disabled={!($session.people < 10)}
        on:click={increment}>+</button
      >
    </div>

    <button
      class="bg-neutral-200 p-3 h-14 rounded-xl font-ridi-serif font-bold text-4xl flex justify-center items-center hover:bg-neutral-300 transition ease-linear anim2"
      on:click={nextSection}>시작하기</button
    >
  </div>
</div>

<script lang="ts">
  import type { Session } from '$lib/stores/sessions';
  import type { Writable } from 'svelte/store';

  export let session: Writable<Session>;

  const decrement = () => $session.people > 1 && ($session.people -= 1);
  const increment = () => $session.people < 10 && ($session.people += 1);

  const nextSection = () => ($session.section += 1);
</script>
