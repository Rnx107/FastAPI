# Learning FastAPI

## Environment

| Component              | Details                |
| ---------------------- | ---------------------- |
| OS                     | Fedora Linux 44        |
| Host                   | Dell Latitude 5410     |
| Kernel                 | 7.0.11-200.fc44.x86_64 |
| Desktop Environment    | GNOME 50.2             |
| Window System          | Wayland                |
| Shell                  | Bash 5.3.9             |
| Terminal               | Ptyxis 50.1            |
| Python Package Manager | uv                     |
| CPU                    | Intel Core i5-10310U   |
| RAM                    | 16 GB                  |
| Filesystem             | Btrfs                  |

## Resources

### Video Tutorials

* Corey Schafer FastAPI Playlist

  * https://www.youtube.com/playlist?list=PL-osiE80TeTsak-c-QsVeg0YYG_0TeyXI

### Documentation

* FastAPI: https://fastapi.tiangolo.com/tutorial/first-steps/
* uv: https://docs.astral.sh/uv/

---

## Day 1: Project Setup

### Setup

* [x] Install uv

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

* [x] Create project

  ```bash
  uv init proj1
  ```

* [x] Install FastAPI

  ```bash
  uv add "fastapi[standard]"
  ```

### FastAPI Basics

* [x] Create root (`/`) route
* [x] Return JSON data
* [x] Return a list from an API endpoint
* [x] Return an HTML response

### Notes

* FastAPI automatically generates API documentation at `/docs`.
* Alternative API documentation is available at `/redoc`.
--
## Day 2
### Notes

* [x] Enable Jinja2 Templating
* [x] pass parameters in HTML Rendering
---
* I learned Django in the past so skipped most of it 
---
