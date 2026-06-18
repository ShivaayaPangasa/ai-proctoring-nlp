from transcript_analyzer import analyze_transcript

transcript = """
Transformers are powerful models.

Furthermore they enable parallel processing.

Therefore they improve efficiency.

Moreover they can capture long-range dependencies.
"""

results = analyze_transcript(transcript)

print(results)