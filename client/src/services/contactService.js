import AxiosFactory from "./Axios";

export const contactService = {
  getContacts: () => { 
    return new Promise(() => {} )
  },
  addContact: (data) => {
    const api = AxiosFactory("contacts");
    return api.post("/", data);
  },
};
