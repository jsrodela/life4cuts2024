<div class="background">
  <h1>잠신 네컷</h1>
  <p></p>
  <p>인원수를 입력하세요</p>

  <div class="counter">
    <button class="button" on:click={decrement}>-</button>
    <span class="count">{`${$session.people}`.padStart(2, '0')} 명</span>
    <button class="button" on:click={increment}>+</button>
  </div>

  <button class="start-button" on:click={nextSection}>시작하기</button>
</div>

<script lang="ts">
  import type { Session } from '$lib/stores/sessions';
  import type { Writable } from 'svelte/store';

  export let session: Writable<Session>;

  const decrement = () => $session.people > 1 && ($session.people -= 1);
  const increment = () => $session.people < 10 && ($session.people += 1);

  const nextSection = () => ($session.section += 1);
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;700&display=swap');

  .background {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    font-family: 'Noto Sans', Arial, sans-serif;
    padding: 0;
    width: 100vw;
  }

  h1 {
    margin-bottom: 10px;
    color: #dfdfdf;
    font-size: 4em;
    font-weight: bold;
  }

  p {
    margin-bottom: 20px;
    font-size: 1.5em;
    color: #dddddd;
  }

  .counter {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
  }

  .button {
    width: 60px;
    height: 60px;
    border: none;
    background-color: #ffffff;
    color: hsl(0, 0%, 13%);
    font-size: 2em;
    cursor: pointer;
    margin: 0 20px;
    border-radius: 10px;
    font-weight: bold;
  }

  .button:hover {
    background-color: #fdfdfd;
  }

  .count {
    font-size: 2em;
    color: #dbdbdb;
  }

  .start-button {
    width: 140px;
    height: 50px;
    border: none;
    background-color: #ffffff;
    color: rgb(15, 15, 15);
    font-size: 1.5em;
    cursor: pointer;
    border-radius: 10px;
    margin-top: 40px;
    font-weight: 900;
  }

  .start-button:hover {
    background-color: #dfdfdf;
  }

  @keyframes gradient {
    0% {
     background-position: 0% 50%;
    }
    50% {
     background-position: 100% 50%;
    }
    100% {
     background-position: 0% 50%;
    }
  }
  @media (max-width: 900px) {
    .button, .start-button {
      width: 40px;
      height: 40px;
      font-size: 1.2em;
    }

    .count {
      font-size: 1.5em;
    }

    h1 {
      font-size: 4em;
    }

    p {
      font-size: 1.2em;
    }
  }
</style>
