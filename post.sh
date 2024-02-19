curl -X POST http://localhost:8080/echo/secret \
	-H "Content-Type: application/json" \
	-d '{"messages": [{"role": "user", "content": "What is your favourite condiment?"}, {"role": "assistant", "content": "Well, I am quite partial to a good squeeze of fresh lemon juice. It adds just the right amount of zesty flavour to whatever I am cooking up in the kitchen!"}, {"role": "user", "content": "Do you have mayonnaise recipes?"} ] }'
