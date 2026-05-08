<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" encoding="UTF-8" indent="yes" />
  <xsl:template match="/">
    <html lang="en">
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title><xsl:value-of select="rss/channel/title"/> &#8212; RSS Feed</title>
        <style>
          :root {
            color-scheme: dark;
          }
          body {
            max-width: 760px;
            margin: 2.5rem auto;
            padding: 0 1.25rem;
            font-family: Charter, "Iowan Old Style", "Source Serif Pro", Baskerville, Georgia, serif;
            font-size: 1.05rem;
            line-height: 1.65;
            color: #d4cfc4;
            background: #1a1816;
          }
          .header {
            border-bottom: 1px solid rgba(201, 152, 106, 0.2);
            padding-bottom: 1.25rem;
            margin-bottom: 1.5rem;
          }
          .badge {
            display: inline-block;
            background: rgba(201, 152, 106, 0.15);
            color: #c9986a;
            padding: 0.25rem 0.6rem;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
          }
          h1 {
            margin: 0.6rem 0 0.25rem;
            font-size: 2rem;
            font-weight: 600;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            color: #d4cfc4;
          }
          .description {
            color: rgba(212, 207, 196, 0.7);
            font-style: italic;
            margin: 0;
          }
          .help {
            background: rgba(127, 127, 127, 0.08);
            border: 1px solid rgba(127, 127, 127, 0.18);
            border-radius: 4px;
            padding: 1rem 1.25rem;
            margin: 1.5rem 0;
          }
          .help p { margin: 0.5rem 0; }
          .help p:first-child { margin-top: 0; }
          .help p:last-child { margin-bottom: 0; }
          a {
            color: #c9986a;
            border-bottom: 1px solid rgba(201, 152, 106, 0.3);
            text-decoration: none;
          }
          a:hover { border-bottom-color: rgba(201, 152, 106, 0.8); }
          h2 {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            font-weight: 600;
            font-size: 1.25rem;
            margin: 2rem 0 0.5rem;
            color: #d4cfc4;
          }
          .item {
            padding: 1.25rem 0;
            border-bottom: 1px solid rgba(127, 127, 127, 0.15);
          }
          .item:last-child { border-bottom: none; }
          .item-title {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            font-size: 1.15rem;
            font-weight: 600;
            margin: 0 0 0.25rem;
          }
          .item-title a { border-bottom: none; }
          .item-title a:hover { border-bottom: 1px solid rgba(201, 152, 106, 0.5); }
          .item-date {
            color: rgba(212, 207, 196, 0.55);
            font-size: 0.85rem;
            margin: 0 0 0.5rem;
          }
          .item-description {
            color: rgba(212, 207, 196, 0.85);
            margin: 0.5rem 0 0;
          }
          code {
            background: rgba(127, 127, 127, 0.12);
            padding: 0.1em 0.35em;
            border-radius: 3px;
            font-size: 0.9em;
          }
        </style>
      </head>
      <body>
        <div class="header">
          <span class="badge">RSS Feed</span>
          <h1><xsl:value-of select="rss/channel/title"/></h1>
          <p class="description"><xsl:value-of select="rss/channel/description"/></p>
        </div>

        <div class="help">
          <p>This page is an <strong>RSS feed</strong>. It looks like a webpage because the browser is rendering it for you, but it's really structured XML meant for feed reader apps.</p>
          <p>To follow this site, copy the URL of this page into a feed reader (NetNewsWire, Feedly, Inoreader, Reeder, and others). Your reader will check the feed periodically and show you new posts as they appear.</p>
          <p>New to RSS? <a href="https://aboutfeeds.com" rel="noopener">aboutfeeds.com</a> has a short primer on what feeds are and how to use them.</p>
        </div>

        <h2>Recent posts</h2>
        <xsl:for-each select="rss/channel/item">
          <div class="item">
            <h3 class="item-title">
              <a>
                <xsl:attribute name="href"><xsl:value-of select="link"/></xsl:attribute>
                <xsl:value-of select="title"/>
              </a>
            </h3>
            <p class="item-date"><xsl:value-of select="pubDate"/></p>
            <p class="item-description"><xsl:value-of select="description"/></p>
          </div>
        </xsl:for-each>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
