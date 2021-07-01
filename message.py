

import discord
async def embed(ctx,user,message):
    embed=discord.Embed(
    title=user,
    color=discord.Color.green())
    # embed.set_author(name="RealDrewData", url="https://twitter.com/RealDrewData", icon_url="https://cdn-images-1.medium.com/fit/c/32/32/1*QVYjh50XJuOLQBeH_RZoGw.jpeg")
    #embed.set_author(name=ctx.author.display_name, url="https://twitter.com/RealDrewData", icon_url=ctx.author.avatar_url)
    # embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
    embed.add_field(name="italics", value=message, inline=False)
    # embed.add_field(name="**Bold**", value="Surround your text in double asterisks (\*\*)", inline=False)
    # embed.add_field(name="__Underline__", value="Surround your text in double underscores (\_\_)", inline=False)
    # embed.add_field(name="~~Strikethrough~~", value="Surround your text in double tildes (\~\~)", inline=False)
    # embed.add_field(name="`Code Chunks`", value="Surround your text in backticks (\`)", inline=False)
    # embed.add_field(name="Blockquotes", value="> Start your text with a greater than symbol (\>)", inline=False)
    # embed.add_field(name="Secrets", value="||Surround your text with double pipes (\|\|)||", inline=False)
    # embed.set_footer(text="Learn more here: realdrewdata.medium.com")
    await ctx.send(embed=embed)

    
