import { writable } from 'svelte/store';

export interface Session {
  people: number,
  frame: string,
  photos: string[],
  width: number, height :number,
  videoLink: string,
  section: number,
  end: boolean
}

export const newSession = () => writable<Session>({
  people: 1,
  frame: "",
  photos: [],
  width: 0, height: 0,
  videoLink: "",
  section: 0, 
  end: false
});
