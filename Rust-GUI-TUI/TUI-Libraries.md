## Rust TUI Libraries/Frameworks
#### Each entry notes whether it needs an external dependency (system library, browser/webview, etc.) to actually run.

- https://github.com/gyscos/cursive
    - A Text User Interface library for the Rust programming language
    - Dependency: requires picking a backend crate (ncurses, pancurses, crossterm, or termion) - the ncurses backend needs the system ncurses library
- https://github.com/ihalila/pancurses
    - A Rust curses library, supports Unix platforms and Windows
    - Dependency: system ncurses (Unix) or bundled PDCurses (Windows)
- https://github.com/veeso/tui-realm
    - A ratatui framework to build stateful applications with a React/Elm inspired approach
    - Dependency: none beyond a terminal - built on ratatui/crossterm
- https://github.com/gdt050579/AppCUI-rs
    - A fast, cross-platform console and text-based user interface (CUI/TUI) framework for Rust
    - Dependency: none - self-contained console engine
- https://github.com/Bristol-Braille/canute-ui-rust
    - Rust elements of UI (experimental)
    - Dependency: targets the Canute Braille e-reader hardware specifically - niche hardware dependency, not a general system library
- https://github.com/mantarias/LabRatUI
    - No description available
- https://github.com/JackDerksen/minui
    - A minimal Rust TUI framework
    - Dependency: none mentioned beyond a terminal (likely crossterm-based)
- https://github.com/johannes-mueller/jilar
    - Johannes' LV2 UI Toolkit for Rust
    - Dependency: an LV2 plugin host / audio-plugin environment (niche, audio-software specific)
- https://github.com/Cedware/bountui
    - A boundary terminal UI
    - Dependency: none beyond a terminal
- https://github.com/TimTheBig/Tuckr-ui
    - No description available
- https://github.com/Grokmoo/thrust-ui
    - Themable Rust UI Toolkit
    - Dependency: unclear from description whether GUI or TUI, or what backend it needs
- https://github.com/crossterm-rs/crossterm
    - Cross platform terminal library for Rust
    - Dependency: none - pure Rust, talks to the terminal directly
- https://github.com/ratatui/ratatui
    - A Rust crate for cooking up terminal user interfaces (TUIs)
    - Dependency: none beyond a terminal - needs a backend crate (crossterm/termion/termwiz), no system library
- https://github.com/ratatui/bevy_ratatui
    - A Rust crate for using Ratatui in a Bevy application
    - Dependency: the Bevy game engine
- https://github.com/ratatui/tachyonfx
    - Effects and animation library for Ratatui applications
    - Dependency: ratatui itself (it's an add-on)
- https://github.com/ratatui/ratzilla
    - Build terminal-themed web applications with Rust and WebAssembly, powered by Ratatui
    - Dependency: runs in a web browser (WASM), not a real terminal

- https://github.com/console-rs/indicatif
    - A command line progress reporting library for Rust
- https://github.com/Joylei/plotters-iced
    - Iced backend for the Plotters charting library

- https://github.com/ad4mx/spinoff
    - Easy to use, robust Rust library for displaying spinners in the terminal
- https://github.com/FGRibreau/spinners
    - 60+ elegant terminal spinners for Rust
- https://github.com/a8m/pb
    - Console progress bar for Rust

- https://github.com/Nukesor/comfy-table
    - Build beautiful terminal tables with automatic content wrapping

- https://github.com/notflan/termprogress
    - A terminal progress bar renderer with status and spinners, in Rust
- https://github.com/abhichavali/zui
    - A minimal and extensible terminal library in Rust
