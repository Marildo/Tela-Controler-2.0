import { Injectable } from '@angular/core';
import { BreakpointObserver, BreakpointState } from '@angular/cdk/layout';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ScreenService {

  constructor(private observer: BreakpointObserver) { }

  isBelowSm(): Observable<BreakpointState> {
    return this.observer.observe(['(max-width: 575px)']);
  }

}
