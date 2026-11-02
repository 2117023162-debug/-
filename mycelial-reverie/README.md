# 蘑幻森林 · Mycelial Reverie

30秒 / 1920×1080 / 30fps / H.264 MP4 / 48kHz双声道配乐 / 中文动态字幕 / 无旁白

故事沿展板的体验逻辑展开：**城市失联 → 脚步唤醒 → 触摸回应 → 身体化为粒子 → 森林共生 → 重新连接**。

- 成片：[renders/mycelial-reverie-30s.mp4](renders/mycelial-reverie-30s.mp4)
- 一键下载工程：[mycelial-reverie-source.zip](../mycelial-reverie-source.zip)
- 分镜与恢复说明：[STORY.md](STORY.md)
- 配色、字体与动效规范：[DESIGN.md](DESIGN.md)
- 检查记录与关键帧：[docs/validation.md](docs/validation.md)

## 预览与重新渲染

需要 Node.js 22+、FFmpeg 和 Chromium/Chrome。HyperFrames 固定为上次使用的 0.8.226 版。

```bash
cd mycelial-reverie
npm ci
npm run dev
npm run check
npm run render -- --output renders/mycelial-reverie-30s.mp4 --fps 30 --quality high --workers 2
```

本云环境已有 `/usr/bin/chromium`，检查与渲染时显式选择它：

```bash
HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm run check
HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm run render -- --output renders/mycelial-reverie-30s.mp4 --fps 30 --quality high --workers 2
```

素材、GSAP和中文字体已包含在 `assets/` 中；渲染不需要重新生成图片或音乐。若修改配乐，安装 NumPy 后在工程目录运行 `python3 make_score.py`。字体为随片文字子集，若添加新的中文字，应重新导出字体子集或换用完整的授权字体。

## 可编辑文件

- `index.html`：六段叙事、字幕、配色、排版和GSAP时间线。
- `world.js`：城市、脚步光环、菌菇、菌丝与人体粒子；基于固定种子、可按时间定位。
- `assets/forest.png`：重新生成的森林场景图。
- `assets/score.wav` 与 `make_score.py`：原创电子氛围配乐与可复现生成脚本。
- `package-lock.json`：安装锁文件。
- `licenses/`：依赖与字体版权说明。

工程包不包含 `node_modules`、缓存和成片；成片MP4单独提供，避免重复下载。

## 恢复记录

2026-11-02，发布后的工作区已不包含旧成片及工程，故按聊天中保留的同一套代码、字幕、时序、视觉规范与配乐参数重建。原森林图片缺失，已重新生成，因此这是一版同方案重渲染，不承诺与旧片逐帧相同。
