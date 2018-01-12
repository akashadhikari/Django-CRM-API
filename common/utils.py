SERVICE_CHOICES = (
	("Hardware", "Hardware"),
	("Software", "Software"),
)

STATUSES = (
	("Pending", "Pending"),
	("Approved", "Approved"),
)

MEDIUM_CHOICES = (
    ("Inbound Call", "Inbound Call"),
    ("Outbound Call", "Outbound Call"),
    ("Inbound Email", "Inbound Email"),
    ("Outbound Email", "Outbound Email"),
    ("Inbound Call", "Inbound Call"),
    ("Outbound Call", "Outbound Call"),
)

YES_NO = (
    ("Successful", "Successful"),
    ("Unsuccessful", "Unsuccessful")
)

SALES_STAGES = (
    ("Suspecting", "Suspecting"), # Contact verification
    ("Prospecting", "Prospecting"), # Client detail
    ("Approaching", "Approaching") # Service intro
)