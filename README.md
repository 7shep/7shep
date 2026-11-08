<h1 align="center">Hi, I'm Alex</h1>
<h3 align="center">A passionate student coding misc projects in his free time!</h3>

- 👯 I’m looking to collaborate on **anything!**

- 👨‍💻 All of my projects are available at [https://alexshepherd.dev](https://alexshepherd.dev)

## 📓 Dev log

<!-- devlog-posts:start -->
**Nov 8** · Yesterday I released mcp-linter v1.1.0, which adds a tool lockfile and diff so it can catch MCP rug pulls, where a server quietly changes its tool definitions after you've approved them. It also gets an install lint, I1, and refuses known-bad releases before launching them. Tools nested over 64 levels are now rejected on every platform, and `run --json` stores a hash of the launch command.

**Nov 7** · This week I added a security lint to mcp-linter, S8, which flags hidden text in MCP tool definitions. Two review findings came out of it, key/value collisions and crashes in the console output, and I fixed both. I also saved the tool lists from the survey runs and added a CLAUDE.md with dev commands and architecture notes. GitHub Actions CI now runs the tests and builds the package on every push.

**Nov 5** · Yesterday I shipped mcp-linter 1.0.0, a tool that checks MCP servers for problems. The last stretch added token-weighted scores per tool and per server, a P4 rule that catches errors returned as success, and a fix so it no longer hands a server my whole environment. I also built a fixing proxy and ran baseline against fixed on 15 held-out tasks, with the results chart at the top of the README.
<!-- devlog-posts:end -->

<details>
<summary>Every commit, last two weeks</summary>

<!-- devlog:start -->
#### Sat, Nov 7
**[mcp-linter](https://github.com/7shep/mcp-linter)**
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

#### Wed, Nov 4
**[mcp-linter](https://github.com/7shep/mcp-linter)**
- Move eval chart to the top
- Release 1.0.0
- Add eval results chart
- Eval results: baseline vs fixed on 15 held-out tasks, descriptions ablation, report
- <sub>[+14 more](https://github.com/7shep/mcp-linter/commits?author=7shep)</sub>

#### Thu, Oct 29
**[newbrain](https://github.com/7shep/newbrain)**
- Stop a second server sharing port 4747 on Windows <sub>`server`</sub>

#### Wed, Oct 28
**[newbrain](https://github.com/7shep/newbrain)**
- Voice controls run headless agents
- Point voice-controls at Brain through its config.json
- Voice controls start background agents
- Ignore voice-controls/ checkout and document it in README

**[voice-controls](https://github.com/7shep/voice-controls)**
- Reopen the mic when it stops sending audio
- Run voice requests as headless agents instead of background sessions
- Catch "Hey Claude" mid-conversation
- Add MIT license
- <sub>[+3 more](https://github.com/7shep/voice-controls/commits?author=7shep)</sub>

#### Tue, Oct 27
**[dfa-drawing](https://github.com/7shep/dfa-drawing)**
- NFA mode: branching brushes, ε-moves, and subset construction
- DFA drawing: automaton art from strings

<sub>Auto-written from my public commits · updated Nov 07, 2026</sub>
<!-- devlog:end -->

</details>

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/7shep" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="7shep" height="30" width="40" /></a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://www.electronjs.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/electron/electron-original.svg" alt="electron" width="40" height="40"/> </a> <a href="https://expressjs.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/express/express-original-wordmark.svg" alt="express" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.java.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" alt="java" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://nativescript.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/nativescript.svg" alt="nativescript" width="40" height="40"/> </a> <a href="https://nodejs.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original-wordmark.svg" alt="nodejs" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://reactjs.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/> </a> <a href="https://tailwindcss.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/tailwindcss/tailwindcss-icon.svg" alt="tailwind" width="40" height="40"/> </a> <a href="https://www.typescriptlang.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-original.svg" alt="typescript" width="40" height="40"/> </a> </p>
