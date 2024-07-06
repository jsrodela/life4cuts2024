import { writable } from 'svelte/store';

interface Session {
  people: number,
  frame: "dark" | "light",
  photos: string[],
  width: number, height :number,
  videoLink: string
}

export const session = writable<Session>({
  people: 1,
  frame: "light",
  photos: [],
  width: 0, height: 0,
  videoLink: ""
});
