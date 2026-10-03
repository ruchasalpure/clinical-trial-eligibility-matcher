from crewai import Agent

clinical_trial_eligibility_matcher = Agent(
    role="Clinical Trial Eligibility Matcher",
    goal="Deliver high-precision autonomous Clinical Trial Eligibility Matcher operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
