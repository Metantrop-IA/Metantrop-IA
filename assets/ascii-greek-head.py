#!/usr/bin/env python3
"""
ASCII Greek Head - Rotating Animation
Vaporwave Edition
"""

import time
import os
import sys

# ANSI color codes for vaporwave colors
PINK = '\033[38;5;205m'
CYAN = '\033[38;5;51m'
PURPLE = '\033[38;5;141m'
YELLOW = '\033[38;5;228m'
RESET = '\033[0m'
BOLD = '\033[1m'

# Different perspectives of the Greek head rotating
frames = [
    # Frame 1: Front view
    """
        ▄▄▄▄▄▄▄▄▄
      ▄▀░░░░░░░░░▀▄
    ▄▀░░░█████░░░░▀▄
   █░░░███████░░░░░█
  █░░░░███████░░░░░█
  █░░░░░█████░░░░░░█
  █░░░░░░███░░░░░░░█
  █░▄▀▀░░░█░░░▀▀▄░░█
  █░█░░░░░░░░░░░█░░█
  █░░▀▄░░░█░░░▄▀░░░█
  █░░░░▀▀███▀▀░░░░░█
  ▀█░░░░░███░░░░░░█▀
   ▀█░░░█████░░░░█▀
    ▀▄░░░███░░░░▄▀
     ▀▄░░░█░░░░▄▀
      ▀▀▄░░░░▄▀▀
        ▀▀▀▀▀
    """,
    # Frame 2: Slight right turn
    """
        ▄▄▄▄▄▄▄▄▄
      ▄▀░░░░░░░░░▀▄
    ▄▀░░░░████░░░░▀▄
   █░░░░██████░░░░░█
  █░░░░░██████░░░░░█
  █░░░░░░████░░░░░░█
  █░░░░░░░██░░░░░░░█
  █░░▀▄░░░█░░░░░░░░█
  █░░░█░░░░░░░░▄▀░░█
  █░░░░▀▄░░█░░█░░░░█
  █░░░░░░▀██▀░░░░░░█
  ▀█░░░░░░██░░░░░░█▀
   ▀█░░░░████░░░░█▀
    ▀▄░░░░██░░░░▄▀
     ▀▄░░░█░░░░▄▀
      ▀▀▄░░░░▄▀▀
        ▀▀▀▀▀
    """,
    # Frame 3: Right side view
    """
        ▄▄▄▄▄▄▄
      ▄▀░░░░░░▀▄
    ▄▀░░░███░░░▀▄
   █░░░████░░░░░█
  █░░░░████░░░░░█
  █░░░░░██░░░░░░█
  █░░░░░░█░░░░░░█
  █░░░▄░░░░░░░░░█
  █░░░█░░░░░░░░░█
  █░░░░▀▄░░░░░░░█
  █░░░░░░▀█▄░░░░█
  ▀█░░░░░░░█░░░█▀
   ▀█░░░░███░░█▀
    ▀▄░░░██░░▄▀
     ▀▄░░█░░▄▀
      ▀▀▄░▄▀▀
        ▀▀▀
    """,
    # Frame 4: Right side profile
    """
        ▄▄▄▄▄
      ▄▀░░░▀▄
    ▄▀░░██░░▀▄
   █░░███░░░░█
  █░░░██░░░░░█
  █░░░░█░░░░░█
  █░░░░░░░░░░█
  █░▄░░░░░░░░█
  █░█░░░░░░░░█
  █░░▀▄░░░░░░█
  █░░░░▀█░░░░█
  ▀█░░░░█░░░█▀
   ▀█░░██░░█▀
    ▀▄░█░░▄▀
     ▀▄█░▄▀
      ▀▄▄▀
       ▀
    """,
    # Frame 5: Back right
    """
        ▄▄▄▄▄
      ▄▀░░░▀▄
    ▄▀░░█░░░▀▄
   █░░░█░░░░░█
  █░░░░░░░░░░█
  █░░░░░░░░░░█
  █░░░░░░░░░░█
  █░░░░░░░░░░█
  █░░░░░░░░░░█
  █░░░░░░░░░░█
  █░░░░░░░░░░█
  ▀█░░░░░░░░█▀
   ▀█░░░░░░█▀
    ▀▄░░░░▄▀
     ▀▄░░▄▀
      ▀▄▄▀
       ▀
    """,
    # Frame 6: Back view
    """
       ▄▄▄▄▄▄▄▄▄
     ▄▀░░░░░░░░░▀▄
   ▄▀░░░█████░░░░▀▄
  █░░░░███████░░░░█
 █░░░░░███████░░░░░█
 █░░░░░░█████░░░░░░█
 █░░░░░░░░█░░░░░░░░█
 █░░░░░░░░░░░░░░░░░█
 █░░░░░░░░░░░░░░░░░█
 █░░░░░░░░░░░░░░░░░█
 █░░░░░░░░░░░░░░░░░█
 ▀█░░░░░░░░░░░░░░░█▀
  ▀█░░░░░░░░░░░░░█▀
   ▀▄░░░░░░░░░░░▄▀
    ▀▄░░░░░░░░░▄▀
     ▀▀▄░░░░▄▀▀
       ▀▀▀▀▀
    """,
    # Frame 7: Back left
    """
        ▄▄▄▄▄
      ▄▀░░░▀▄
    ▄▀░░░█░░▀▄
   █░░░░░█░░░█
  █░░░░░░░░░░█
  █░░░░░░░░░░█
  █░░░░░░░░░░█
  █░░░░░░░░░░█
  █░░░░░░░░░░█
  █░░░░░░░░░░█
  █░░░░░░░░░░█
  ▀█░░░░░░░░█▀
   ▀█░░░░░░█▀
    ▀▄░░░░▄▀
     ▀▄░░▄▀
      ▀▄▄▀
       ▀
    """,
    # Frame 8: Left side profile
    """
         ▄▄▄▄▄
       ▄▀░░░▀▄
     ▄▀░░██░░▀▄
    █░░░███░░░█
   █░░░░██░░░░█
   █░░░░█░░░░░█
   █░░░░░░░░░░█
   █░░░░░░░░▄░█
   █░░░░░░░░█░█
   █░░░░░░▄▀░░█
   █░░░░█▀░░░░█
   ▀█░░░█░░░░█▀
    ▀█░░██░░█▀
     ▀▄░░█░▄▀
      ▀▄░█▄▀
       ▀▄▄▀
        ▀
    """,
    # Frame 9: Left side view
    """
         ▄▄▄▄▄▄▄
       ▄▀░░░░░░▀▄
     ▄▀░░░███░░░▀▄
    █░░░░████░░░░█
   █░░░░████░░░░░█
   █░░░░░██░░░░░░█
   █░░░░░█░░░░░░░█
   █░░░░░░░░░░▄░░█
   █░░░░░░░░░░█░░█
   █░░░░░░░░▄▀░░░█
   █░░░░░▄█▀░░░░░█
   ▀█░░░█░░░░░░░█▀
    ▀█░░███░░░░█▀
     ▀▄░░██░░░▄▀
      ▀▄░░█░░▄▀
       ▀▀▄░▄▀▀
         ▀▀▀
    """,
    # Frame 10: Slight left turn
    """
         ▄▄▄▄▄▄▄▄▄
       ▄▀░░░░░░░░░▀▄
     ▄▀░░░░████░░░░▀▄
    █░░░░░██████░░░░█
   █░░░░░░██████░░░░█
   █░░░░░░░████░░░░░█
   █░░░░░░░░██░░░░░░█
   █░░░░░░░░█░░░▄▀░░█
   █░░▀▄░░░░░░░█░░░░█
   █░░░░█░░█░░▄▀░░░░█
   █░░░░░░▀██▀░░░░░░█
   ▀█░░░░░░██░░░░░░█▀
    ▀█░░░░████░░░░█▀
     ▀▄░░░░██░░░░▄▀
      ▀▄░░░░█░░░▄▀
       ▀▀▄░░░░▄▀▀
         ▀▀▀▀▀
    """,
]

def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def colorize_frame(frame, color_index):
    """Apply vaporwave colors to the frame"""
    colors = [PINK, CYAN, PURPLE, YELLOW]
    color = colors[color_index % len(colors)]
    return f"{BOLD}{color}{frame}{RESET}"

def print_header():
    """Print the vaporwave header"""
    print(f"\n{BOLD}{PINK}╔═══════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{CYAN}║  ◆ Ｇ Ｒ Ｅ Ｅ Ｋ  Ｈ Ｅ Ａ Ｄ ◆  ║{RESET}")
    print(f"{BOLD}{PURPLE}║   ═══ Ｖ Ａ Ｐ Ｏ Ｒ Ｗ Ａ Ｖ Ｅ ═══   ║{RESET}")
    print(f"{BOLD}{PINK}╚═══════════════════════════════════════╝{RESET}\n")

def print_footer():
    """Print the vaporwave footer"""
    print(f"\n{BOLD}{CYAN}════════════════════════════════════════{RESET}")
    print(f"{BOLD}{PURPLE}Press Ctrl+C to exit{RESET}")

def animate():
    """Main animation loop"""
    frame_index = 0
    color_index = 0
    
    try:
        while True:
            clear_screen()
            print_header()
            
            # Get current frame and colorize it
            current_frame = frames[frame_index]
            colored_frame = colorize_frame(current_frame, color_index)
            print(colored_frame)
            
            print_footer()
            
            # Update indices
            frame_index = (frame_index + 1) % len(frames)
            color_index = (color_index + 1) % 4
            
            # Wait before showing next frame
            time.sleep(0.3)
            
    except KeyboardInterrupt:
        clear_screen()
        print(f"\n{BOLD}{PINK}◆ {CYAN}Ｇ Ｏ Ｏ Ｄ Ｂ Ｙ Ｅ{PINK} ◆{RESET}\n")
        sys.exit(0)

if __name__ == "__main__":
    print(f"\n{BOLD}{CYAN}Starting ASCII Greek Head Animation...{RESET}")
    time.sleep(1)
    animate()
