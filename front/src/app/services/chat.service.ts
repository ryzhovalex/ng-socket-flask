import { Injectable } from "@angular/core";
import { Socket } from "ngx-socket-io";
import { map } from "rxjs/operators";


@Injectable({
  providedIn: "root"
})
export class ChatService {

  constructor(private socket: Socket) { }

  sendMessage(msg: string) {
    console.log("send message: " + msg)
    this.socket.emit("message", msg);
  }

  getMessage() {
    return this.socket.fromEvent("message").pipe(map((data: any) => data));
  }

  join() {
    console.log("join")
    this.socket.emit("join", "hello")
  }
}
