
TOP_10 = [
    "El Diego",
    "Bilardo",
    "Charly García",
    "El Flaco Spinneta",
    "El Gato 🐈‍⬛ Gaudio",
    "Willy Villas",
    "Bianchi",
    "El Negro Olmedo",
    "Fito Páez",
    "Fangio",
    "Evita",
    "Messi",
    "El General Perón",
    "Favaloro",
    "Juan Martín Del Potro",
    "Monzón",
    "Susana Giménez",
    "El Flaco Traverso",
    "David Nalbandián",
    "Ceratti",
]
def top10arg(update, bot):
    text_msg = "```\n" + "\n".join([f"{i:02}) {x}" for i, x in enumerate(TOP_10, 1)]) + "```"
    update.message.reply_text(text_msg, parse_mode="Markdown")
