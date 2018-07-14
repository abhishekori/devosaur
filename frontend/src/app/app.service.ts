import { Injectable } from '@angular/core';
import {HttpHeaders, HttpClient} from '@angular/common/http'
import { Observable } from 'rxjs';

const httpOptions={
  headers:new HttpHeaders({
    'Content-Type':'application/json'
  })
}
const apiUrl='http://localhost:5000'

@Injectable()
export class AppService {
  constructor(
    private http:HttpClient
  ) { }

  postRequest(url:string,body:any):Observable<any>{
    
    return this.http.post<any>(apiUrl+url,body,httpOptions);
  }
}
