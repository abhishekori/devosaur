import { Component, OnInit } from '@angular/core';
import { AppService } from '../app.service';

@Component({
  selector: 'app-create-project',
  templateUrl: './create-project.component.html',
  styleUrls: ['./create-project.component.css']
})
export class CreateProjectComponent implements OnInit {

  constructor(private appService:AppService) { }
  model:any={}

  createProject(){

    const url='/create-project'
    this.appService.postRequest(url,this.model).subscribe((data)=>{
      console.log(data)
    })
    //console.log(this.model)
  }

  ngOnInit() {
  }

}
