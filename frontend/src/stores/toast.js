import { defineStore } from "pinia";

export const useToastStore = defineStore("toast", {
  state: () => ({
    time: 0,
    message: "",
    classes: "",
    isvisible: false,
  }),
  
  actions: {
    showToast(time, message, classes) {
      this.time = parseInt(time);
      this.message = message
      this.classes = classes,
      this.isvisible = true;
    },
  },
});
