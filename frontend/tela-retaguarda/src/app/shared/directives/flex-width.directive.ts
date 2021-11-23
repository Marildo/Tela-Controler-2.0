import {
  BreakpointObserver,
  Breakpoints,
  BreakpointState,
} from '@angular/cdk/layout';
import { Directive, HostBinding, Input, OnInit } from '@angular/core';

@Directive({
  selector: '[utFlexWidth]',
})
export class FlexWidth implements OnInit {
  @Input() xs: string = '';
  @Input() sm: string = '';
  @Input() md: string = '100';
  @Input() lg: string = '';
  @Input() xl: string = '';

  @HostBinding('style.width') width: string = '';

  constructor(private breakpointObserver: BreakpointObserver) {}

  ngOnInit(): void {
    const breakpoints: Array<string> = [
      Breakpoints.XSmall,
      Breakpoints.Small,
      Breakpoints.Medium,
      Breakpoints.Large,
      Breakpoints.XLarge,
    ];

    this.breakpointObserver
      .observe(breakpoints)
      .subscribe((state: BreakpointState) => {
        if (state.breakpoints[Breakpoints.XSmall]) {
          if (this.xs != '') {
            this.width = this.xs;
          } else if (this.sm != '') {
            this.width = this.sm;
          } else {
            this.width = this.md;
          }
        }

        if (state.breakpoints[Breakpoints.Small]) {
          if (this.sm != '') {
            this.width = this.sm;
          } else {
            this.width = this.md;
          }
        }

        if (state.breakpoints[Breakpoints.Medium]) {
          if (this.md != '') {
            this.width = this.md;
          }
        }

        if (state.breakpoints[Breakpoints.Large]) {
          if (this.lg != '') {
            this.width = this.lg;
          } else {
            this.width = this.md;
          }
        }

        if (state.breakpoints[Breakpoints.XLarge]) {
          if (this.xl != '') {
            this.width = this.xl;
          } else if (this.lg != '') {
            this.width = this.lg;
          } else {
            this.width = this.md;
          }
        }
      });
  }
}
