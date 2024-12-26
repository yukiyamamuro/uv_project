from pegasus import Pegasus

pegasus = Pegasus(
    output_dir="output_directory",
    exclude_selectors=["header", "footer", "nav"],
    include_domain="example.com",
    exclude_keywords=["login"],
    output_extension=".txt",
    dust_size=500,
    max_depth=2,
    system_message="You are an assistant to determine if the content of a given website contains useful information related to a specific topic. If it contains relevant and beneficial information about the topic, answer 'True', otherwise answer 'False'.",
    classification_prompt="Does the content of the following website provide beneficial information about the Roomba API or iRobot? If so, answer 'True', if not, answer 'False'.",
    max_retries=5,
    model="gemini/gemini-1.5-pro-latest",
    rate_limit_sleep=30,
    other_error_sleep=5,
)
pegasus.run("https://example.com/start-page")
