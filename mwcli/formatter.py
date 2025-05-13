def format_definition(word, entries):
    if not entries or not isinstance(entries[0], dict):
        return f"No exact match found for '{word}'. Suggestions: {', '.join(entries)}"

    entry = entries[0]
    pronunciation = entry.get('hwi', {}).get('prs', [{}])[0].get('mw', 'N/A')
    part_of_speech = entry.get('fl', 'N/A')
    definition = entry.get('shortdef', ['N/A'])[0]

    return (f"\n📖 {word}\n"
            f"📌 Pronunciation: {pronunciation}\n"
            f"🧠 Part of Speech: {part_of_speech}\n"
            f"💬 Definition: {definition}")

