<h1 align="center">Hi, I'm Alex</h1>
<h3 align="center">A passionate student coding misc projects in his free time!</h3>

- 👯 I’m looking to collaborate on **anything!**

- 👨‍💻 All of my projects are available at [https://alexshepherd.dev](https://alexshepherd.dev)

## 📓 Dev log

<!-- devlog-posts:start -->
**Nov 16** · Yesterday I rebuilt my personal site, dev-website, into something more like a generative gallery. The hero and projects got restyled, and I added a Clubs section, trimmed the featured projects, and made the About section live. I also moved the sections around and removed the contact one. On the Spotify side, token refresh now trims env values and logs the OAuth error code when it fails.

**Nov 15** · Yesterday I built Lucent, a Dynamic-Island-style now-playing pill for Windows 11. It now has a song timeline in the expanded island and a mini timeline on the pill itself. The window is shaped so clicks pass through the transparent area, and the pill hides or moves when an app goes fullscreen. I also made media startup retry with backoff and moved thumbnail reads onto a worker thread with a timeout.

**Nov 12** · Yesterday I added a runtime trifecta guard to mcp-linter's mcp-lint proxy, with off, warn and block modes, and made it fail closed if the tool list never settles before a call. I also built a holdout of 6 new servers with blind labels to score the trifecta tagger, then drafted a v2 tagger for data third parties write into. The full Haiku 5.5 trifecta run came back a null result, and I recorded it anyway.
<!-- devlog-posts:end -->

<details>
<summary>Every commit, last two weeks</summary>

<!-- devlog:start -->
#### Sat, Nov 14
**[lucent](https://github.com/7shep/lucent)**
- Show a mini timeline on the pill, fix paused icon (#15) <sub>`pill`</sub>
- Hide with SW_HIDE to match the raw show
- Keep the pill put when it is clicked; show without activating
- Rebuild the hit region when the pill changes monitor or DPI
- <sub>[+11 more](https://github.com/7shep/lucent/commits?author=7shep)</sub>

#### Wed, Nov 11
**[mcp-linter](https://github.com/7shep/mcp-linter)**
- Claude bridge: kill the whole session tree on a trial timeout
- Local runner: add a hash of the model id to its logdir
- Add the Claude Code bridge for AgentDojo: plan login, no API key
- Local runner: actually run trials, one logdir per model
- <sub>[+9 more](https://github.com/7shep/mcp-linter/commits?author=7shep)</sub>

#### Tue, Nov 10
**[mcp-linter](https://github.com/7shep/mcp-linter)**
- Score v1 and the draft v2 tagger on the blind holdout
- Add the tagger holdout: 6 new servers and blind labels
- Add a runtime trifecta guard to mcp-lint proxy (--guard off|warn|block)
- Draft a v2 trifecta tagger for data third parties write into
- <sub>[+3 more](https://github.com/7shep/mcp-linter/commits?author=7shep)</sub>

#### Sun, Nov 8
**[mcp-linter](https://github.com/7shep/mcp-linter)**
- Add trifecta benchmark mock servers and offline harness
- Add trifecta benchmark design and tagging prototype
- Fix CI: ExceptionGroup on Python 3.10, mcp-lint path outside a venv

#### Sat, Nov 7
**[mcp-linter](https://github.com/7shep/mcp-linter)**
- Add Streamable HTTP transport, a lock-check Action and PyPI releases
- Release v1.1.0; run --json stores a hash of the launch command
- Add install lint (I1) and refuse known-bad releases before launch
- Reject tools nested over 64 levels on every platform

#### Fri, Nov 6
**[mcp-linter](https://github.com/7shep/mcp-linter)**
- CLAUDE.md: describe lock.py
- Add tool lockfile and diff to catch MCP rug pulls
- Add CLAUDE.md with dev commands and architecture notes
- Add GitHub Actions CI for tests and package build
- <sub>[+2 more](https://github.com/7shep/mcp-linter/commits?author=7shep)</sub>

<sub>Auto-written from my public commits · updated Nov 15, 2026</sub>
<!-- devlog:end -->

</details>

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/7shep" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="7shep" height="30" width="40" /></a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://www.electronjs.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/electron/electron-original.svg" alt="electron" width="40" height="40"/> </a> <a href="https://expressjs.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/express/express-original-wordmark.svg" alt="express" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.java.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" alt="java" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://nativescript.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/nativescript.svg" alt="nativescript" width="40" height="40"/> </a> <a href="https://nodejs.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original-wordmark.svg" alt="nodejs" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://reactjs.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/> </a> <a href="https://tailwindcss.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/tailwindcss/tailwindcss-icon.svg" alt="tailwind" width="40" height="40"/> </a> <a href="https://www.typescriptlang.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-original.svg" alt="typescript" width="40" height="40"/> </a> </p>
