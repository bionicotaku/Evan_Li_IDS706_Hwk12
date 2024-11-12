def generate_markdown(output):    
    # Generate markdown content
    markdown_content = "# Data Analysis Results\n\n"

    # Add code output
    markdown_content += "## Statistical Analysis\n\n"
    markdown_content += "```\n" + output + "```\n\n"

    # # Add images
    # image_files = [
    #     "salary_distribution.png",
    #     "job_title_distribution.png",
    #     "experience_level_distribution.png",
    #     "average_salary_by_job.png",
    #     "salary_vs_experience.png"
    # ]

    # for image in image_files:
    #     markdown_content += (
    #         f"![{image.split('.')[0].replace('_', ' ').title()}]"
    #         f"(output/{image})\n\n"
    #     )

    # Write markdown content to file
    with open("analysis_results.md", "w") as md_file:
        md_file.write(markdown_content)