from prompt2model.prompt_parser import MockPromptSpec, TaskType
from prompt2model.dataset_retriever import DescriptionDatasetRetriever

if __name__ == "__main__":
    prompt_spec = MockPromptSpec(TaskType.TEXT_GENERATION)
    # prompt_spec._instruction = """Verify scientific claims automatically as fact or fiction. Provide supporting evidence with your decision.."""
    prompt = """Your task is to generate an answer to a natural question. In this task, the input is a string that consists of both a question and a context passage. The context is a descriptive passage related to the question and contains the answer. And the question can range from Math, Cultural, Social, Geometry, Biology, History, Sports, Technology, Science, and so on."""
    prompt_spec._instruction = prompt

    retriever = DescriptionDatasetRetriever()
    # retriever.encode_dataset_descriptions(retriever.search_index_path)
    retriever.retrieve_dataset_dict(prompt_spec, blocklist="squad")