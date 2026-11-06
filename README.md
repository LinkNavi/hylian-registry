# hylian-registry

A [Mason](https://github.com/mason-org/mason.nvim) registry for Hylian tooling.

## Use it

```lua
require("mason").setup({
  registries = {
    "github:LinkNavi/hylian-registry",
    "github:mason-org/mason-registry", -- keep the default registry too
  },
})
```

Then `:MasonUpdate` and `:MasonInstall hylian-lsp`.

Mason only installs the binary. Start it with (Neovim 0.11+):

```lua
vim.filetype.add({ extension = { hy = "hylian" } })
vim.lsp.config("hylian", { cmd = { "hylian-lsp" }, filetypes = { "hylian" }, root_markers = { ".git" } })
vim.lsp.enable("hylian")
```

## Maintain it

- Cut a release of the language server: push tag `lsp-vX.Y.Z` in LinkNavi/Hylian (its workflow attaches `hylian-lsp-linux-x64.tar.gz`).
- Bump `source.id` in `packages/hylian-lsp/package.yaml` to that tag, push to `main`; the workflow publishes a new `registry.json.zip` release.
- Test locally: `python3 scripts/build.py`, then `registries = { "file:/path/to/hylian-registry" }`.
