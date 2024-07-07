import { writable } from 'svelte/store';

export interface Session {
  people: number,
  frame: "dark" | "light",
  photos: string[],
  width: number, height :number,
  videoLink: string,
  section: number
}

export const newSession = () => writable<Session>({
  people: 1,
  frame: "light",
  photos: [],
  width: 0, height: 0,
  videoLink: "",
  section: 0
});
