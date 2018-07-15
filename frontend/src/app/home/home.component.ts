import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor() { }
  profleImgUrl:string='https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Lilium_kesselringianum_in_Sochi.jpg/128px-Lilium_kesselringianum_in_Sochi.jpg';

  ngOnInit() {
  }

}
