-- Append the canary UUID as the last block of every document so it
-- ends up inside the main content body (not a separate footer widget)
-- and gets picked up by readability-style content extractors.

function Pandoc(doc)
  local uuid = pandoc.Para({pandoc.Str("979af0cf-9d1e-4435-bfc4-8cb8a4cf8c7b")})
  local wrapper = pandoc.Div({uuid}, pandoc.Attr("", {"page-uuid"}, {}))
  table.insert(doc.blocks, wrapper)
  return doc
end
