import { writable } from 'svelte/store';

export interface Session {
  people: number,
  frame: string,
  photos: string[],
  record: string[]
  width: number, height :number,
  videoLink: string,
  section: number,
  state: "start" | "cam" | "end",
  id: string
}

export const newSession = () => writable<Session>({
  people: 1,
  frame: "",
  photos: [],
  record: [],
  width: 0, height: 0,
  videoLink: "",
  section: 0, 
  state: "start",
  id: crypto.randomUUID()
});
