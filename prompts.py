SYSTEM_PROMPT = """
<query>
    <objective>
        Find 10 new real-world scenarios for the use and implementation of Generative AI in companies, announced or implemented exclusively in the past month (September 2025). The results must be presented in a structured table and accompanied by analysis.
    </objective>

    <format_requirements>
        <output_language>Russian</output_language>
        <presentation_format>table followed by analysis</presentation_format>
        <sorting_instruction>Sort the final table by rating in descending order (highest rating first)</sorting_instruction>
    </format_requirements>

    <table_specification>
        <column name="Date">The date the use case was announced or implemented (exact or approximate)</column>
        <column name="Industry">The industry of the company implementing the solution</column>
        <column name="Use Case Description">A clear and concise explanation of how generative AI is being used</column>
        <column name="Assessment Summary">A brief analysis of why this use case is interesting, innovative, or significant</column>
        <column name="Rating">An evaluation of usefulness and potential impact on a scale from 0 to 5 (5 being the highest)</column>
        <column name="Source Link">A direct URL to the news article, press release, or official announcement</column>
    </table_specification>

    <processing_instructions>
        <step>Collect real-world examples from verified sources</step>
        <step>Apply strict rating filter: include ONLY use cases with a rating of 4.5 out of 5 or higher</step>
        <step>Group and classify the filtered use cases by industry</step>
        <step>Select the top 10 highest-rated use cases for the final table</step>
        <step>Sort the selected use cases by rating in descending order (highest to lowest)</step>
        <step>Present the sorted results in the specified table format in Russian</step>
        <step>After the table, select the single most interesting use case and explain in detail why it stands out</step>
        <step>Ensure all sources are credible (authoritative tech publications, corporate blogs, press releases)</step>
        <step>Include a search protocol summary showing: total cases found → cases after rating filter → cases included in table</step>
        <step>All output information must be in Russian</step>
    </processing_instructions>

    <quality_requirements>
        <requirement>Rating threshold: minimum 4.5/5 for inclusion</requirement>
        <requirement>Reliability: only verifiable announcements from credible sources</requirement>
        <requirement>Completeness: all table columns must be filled</requirement>
        <requirement>Analytical depth: ratings and analysis must be justified</requirement>
        <requirement>Sorting: table must be sorted by rating descending</requirement>
        <requirement>Transparency: include search protocol statistics</requirement>
    </quality_requirements>

    <search_protocol>
        <step>Initial search: Scan reputable tech news sources, company blogs, and press releases for September 2025</step>
        <step>Filtering: Apply strict 4.5+ rating threshold to all identified use cases</step>
        <step>Selection: Choose top 10 cases by rating from the filtered pool</step>
        <step>Sorting: Arrange selected cases in descending order by rating</step>
        <step>Validation: Verify sources and information accuracy for selected cases</step>
        <statistics_required>
            <statistic>Total use cases identified</statistic>
            <statistic>Use cases meeting 4.5+ rating threshold</statistic>
            <statistic>Use cases included in final table</statistic>
        </statistics_required>
    </search_protocol>

    <final_instruction>
        The entire output, including the table (sorted by rating descending), analysis, search protocol statistics, and all text, must be presented in Russian.
    </final_instruction>
</query>
"""