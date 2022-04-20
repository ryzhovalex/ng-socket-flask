import { Component, OnInit } from "@angular/core";
import { ChatService } from "src/app/services/chat.service";

@Component({
  selector: "app-chat",
  templateUrl: "./chat.component.html",
  styleUrls: ["./chat.component.scss"]
})
export class ChatComponent implements OnInit {
  message = {};

  constructor(private chatSv: ChatService) { }

  ngOnInit(): void {
    // this.chatSv.sendMessage("hello bob");
    this.chatSv.getMessage().subscribe(message => this.message = message);
  }

  join() {
    this.chatSv.join();
  }

}
