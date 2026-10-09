# Echo Hub Theme

A calm, Echo Show–style Home Assistant theme with light and dark modes. It is the theme for the [Echo Hub dashboard](https://github.com/DynamotechLLC/echo-hub), and works as an everyday theme on its own.

| Light | Dark |
|---|---|
| ![Echo Hub, light](https://raw.githubusercontent.com/DynamotechLLC/echo-hub/main/docs/screenshots/echo-hub-light.jpg) | ![Echo Hub, dark](https://raw.githubusercontent.com/DynamotechLLC/echo-hub/main/docs/screenshots/echo-hub-dark.jpg) |

## Install with HACS

1. HACS → ⋮ → **Custom repositories** → add `DynamotechLLC/echo-hub-ha-theme`, category **Theme**.
2. Open **Echo Hub Theme** in HACS and **Download**.
3. Developer tools → **Actions** → run `frontend.reload_themes`.

## Manual install

Copy `themes/echo-hub.yaml` into `config/themes/`, then run `frontend.reload_themes`.

## `configuration.yaml`

Themes must be loaded from the `themes` folder. If you have not done this already, add:

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

and restart Home Assistant.

## Select it

Profile → **Browser settings** → **Theme** → **Echo Hub**. Set **Dark mode** to Auto, Light or Dark.

## Make it the default

Run `frontend.set_theme` twice, once per mode:

```yaml
action: frontend.set_theme
data:
  name: Echo Hub
  mode: light
```

```yaml
action: frontend.set_theme
data:
  name: Echo Hub
  mode: dark
```

## Font

The theme uses [Figtree](https://fonts.google.com/specimen/Figtree). Add it as a dashboard resource (Settings → Dashboards → ⋮ → **Resources** → Add, type **Stylesheet**):

```
https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&display=swap
```

Without it the system font is used.

## Variables

The Echo Hub dashboard reads these `--echo-*` variables. Use them in your own cards with `var(--echo-accent)`.

| Variable | Light | Dark |
|---|---|---|
| `--echo-accent` | `#1E8BB0` | `#1E8BB0` |
| `--echo-accent-deep` | `#136F8F` | `#136F8F` |
| `--echo-heat` | `#E5484D` | `#E5484D` |
| `--echo-cool` | `#2F80ED` | `#2F80ED` |
| `--echo-ok` | `#2E9E6B` | `#2E9E6B` |
| `--echo-warn` | `#E8A33D` | `#E8A33D` |
| `--echo-home` | `#2E8B6E` | `#2E8B6E` |
| `--echo-tile` | `#F4F6F8` | `#1C252E` |
| `--echo-panel` | `rgba(255, 255, 255, 0.35)` | `rgba(255, 255, 255, 0.05)` |
| `--echo-pill` | `rgba(255, 255, 255, 0.78)` | `rgba(28, 37, 46, 0.9)` |

## License

[MIT](LICENSE) © 2026 DynamotechLLC
