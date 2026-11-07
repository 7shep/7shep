<h1 align="center">Hi, I'm Alex</h1>
<h3 align="center">A passionate student coding misc projects in his free time!</h3>

- 👯 I’m looking to collaborate on **anything!**

- 👨‍💻 All of my projects are available at [https://alexshepherd.dev](https://alexshepherd.dev)

## 📓 Dev log

<!-- devlog-posts:start -->
**Nov 5** · Yesterday I shipped mcp-linter 1.0.0, a tool that checks MCP servers for problems. The last stretch added token-weighted scores per tool and per server, a P4 rule that catches errors returned as success, and a fix so it no longer hands a server my whole environment. I also built a fixing proxy and ran baseline against fixed on 15 held-out tasks, with the results chart at the top of the README.

**Nov 4** · Yesterday I built mcp-linter, a tool that connects to an MCP server and checks it for problems. It has static rules for tool definitions, plus probe rules that call tools and flag things like errors returned as success, opaque IDs, and missing paging hints. It also gives token-weighted scores per tool and per server. I ran it against 10 third-party MCP servers to see how it holds up.

**Oct 30** · Yesterday's only commit was in newbrain, a fix for the server on Windows. A second server could bind to port 4747 while one was already running, so two copies could end up sharing it. I changed it so that no longer happens. It's a small change, but it means the app only ever answers from one process.
<!-- devlog-posts:end -->

<details>
<summary>Every commit, last two weeks</summary>

<!-- devlog:start -->
#### Fri, Nov 6
**[mcp-linter](https://github.com/7shep/mcp-linter)**
- Add CLAUDE.md with dev commands and architecture notes
- Add GitHub Actions CI for tests and package build
- Fix two S8 review findings: key/value collisions and console crashes
- Add S8 hidden-text security lint and save survey tool lists

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

#### Mon, Oct 26
**[newbrain](https://github.com/7shep/newbrain)**
- Morning dev log post on the GitHub profile README <sub>`agents`</sub>
- Give every comment target a working link <sub>`linkedin`</sub>

<sub>Auto-written from my public commits · updated Nov 07, 2026</sub>
<!-- devlog:end -->

</details>

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/7shep" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="7shep" height="30" width="40" /></a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://www.electronjs.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/electron/electron-original.svg" alt="electron" width="40" height="40"/> </a> <a href="https://expressjs.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/express/express-original-wordmark.svg" alt="express" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.java.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" alt="java" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://nativescript.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/nativescript.svg" alt="nativescript" width="40" height="40"/> </a> <a href="https://nodejs.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original-wordmark.svg" alt="nodejs" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://reactjs.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/> </a> <a href="https://tailwindcss.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/tailwindcss/tailwindcss-icon.svg" alt="tailwind" width="40" height="40"/> </a> <a href="https://www.typescriptlang.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-original.svg" alt="typescript" width="40" height="40"/> </a> </p>
