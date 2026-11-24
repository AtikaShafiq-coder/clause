# from  langchain.agents import create_agent 
# from langchain.messages import HumanMessage
# from langchain.tools import tool

# from app.services.chat import RAGService

# class ClauseAgent:

#     def __init__(self)->None:    
#         self.rag = RAGService()  #instance attribute class type if we  set None then abhi humnay ismay rag ka concept implement nhi kiya   baad mai hum rkhty hain 

#         @tool(response_format="content_and_artifact")
#         def search_handbook(question:str):
#             """this function...."""
#             result = self.rag.store.similarity_search_with_score(
#                 query=question,
#                 k=self.rag.settings.top_k
#             )
#             if not result:
#                 return "Nothing Found",[]

#             texts = []
#             sources = []
#             for doc,score in result:
#                 texts.append(doc.page_content)
#                 sources.append({"source": doc.metadata.get("source"),"page": doc.metadata.get("page"),"score":round(number=score, ndigits=4)})
#             text = "\n\n".join(texts) #string object
#             return text, sources
#         self.agent = create_agent(
#             model=self.rag.llm,
#             tools=[search_handbook],
#             system_prompt=self.rag.settings.system_prompt
#         )

#     def ask(self, question:str):
#         result = self.agent.invoke(input={"messages":[HumanMessage(content=question)]})
#         messages = result["messages"]

#         answer = messages[-1].text
#         return answer

#     def close(self):
#         self.rag.close()


# from langchain.agents import create_agent
# from langchain.messages import HumanMessage
# from langchain.tools import tool


# from app.core.config import get_settings
# from app.prompts.loader import get_prompt
# from app.llm.models import get_chat_model
# from app.rag.vectorstore import get_vector_store



# class ClauseAgent:
#     def __init__(self) -> None:
#         self.settings = get_settings()
#         self.client = get_vector_store(settings=self.settings)

#         @tool(response_format="content_and_artifact")
#         def search_handbook(question: str):
#             """Search the Clause shop handbook: refunds, delivery times and fees,
#             payments, cash on delivery, warranty, exchanges, tracking, loyalty, support hours.
#             Use a short query like "refund window electronics"."""
#             results = self.store.similarity_search_with_score(
#                 query=question,
#                 k=self.settings.top_k,
#             )
#             if not results:
#                 return "Nothing found.", []

#             texts = []
#             sources = []
#             for doc, score in results:
#                 texts.append(doc.page_content)
#                 sources.append(
#                     {
#                         "sources": doc.metadata.get("sources"),
#                         "page": doc.metadata.get("page"),
#                         "score": round(number=score, ndigits=4),
#                     }
#                 )

#             combined_text = "\n\n".join(texts)
#             return combined_text, sources

#         self.agent = create_agent(
#             model=self.llm,
#             tools=[search_handbook],
#             system_prompt=get_prompt(
#                 name="support/system",
#                 version=self.settings.system_prompt_version
#             )
#         )

#     def ask(self, question: str) -> str:
#         result = self.agent.invoke({"messages": [HumanMessage(content=question)]})
#         messages = result["messages"]
#         return messages[-1].text
    

#     def close(self) -> None:
#         self.store.client.close()



# from langchain.agents import create_agent
# from langchain.messages import HumanMessage
# from langchain.tools import tool

# from app.core.config import get_settings
# from app.prompts.loader import get_prompt
# from app.llm.models import get_chat_model
# from app.rag.vectorstore import get_vector_store


# class ClauseAgent:
#     def __init__(self) -> None:
#         self.settings = get_settings()
#         self.client =  get_vector_store(settings=self.settings)

#         @tool(response_format="content_and_artifact")
#         def search_handbook(question: str):
#             """Search the Clause shop handbook: refunds, delivery times and fees,
#             payments, cash on delivery, warranty, exchanges, tracking, loyalty, support hours.
#             Use a short query like "refund window electronics"."""
#             results = self.store.similarity_search_with_score(
#                 query=question,
#                 k=self.rag.settings.top_k,
#             )
#             if not results:
#                 return "Nothing found.", []

#             texts = []
#             sources = []
#             for doc, score in results:
#                 texts.append(doc.page_content)
#                 sources.append(
#                     {
#                         "sources": doc.metadata.get("sources"),
#                         "page": doc.metadata.get("page"),
#                         "score": round(score, 4),
#                     }
#                 )

#             combined_text = "\n\n".join(texts)
#             return combined_text, sources

#         self.agent = create_agent(
#             model=get_chat_model(settings=self.settings),
#             tools=[search_handbook],
#             system_prompt=get_prompt(
#                 name="support/system",
#                 version=self.settings.system_prompt_version
#                 )
#         )

#     def ask(self, question: str) -> str:
#         result = self.agent.invoke({"messages": [HumanMessage(question)]})
#         messages = result["messages"]
#         return messages[-1].text

#     def close(self) -> None:
#         self.store.client.close()


from langchain.agents import create_agent
from langchain.messages import HumanMessage
# from langchain.tools import tool
from app.core.config import get_settings
from app.prompts.loader import get_prompt
from app.llm.models import get_chat_model
from app.rag.vectorstore import get_vector_store
from app.tools.knowledge.handbook import file_search
from app.middleware.stacks import default_stack


class ClauseAgent:
    def __init__(self) -> None:
        self.settings = get_settings()
        self.store = get_vector_store(settings=self.settings)

        # @tool(response_format="content_and_artifact")
        # def search_handbook(question: str):
        #     """Search the Clause shop handbook for refunds, delivery,
        #     payments, COD, warranty, exchanges, tracking, loyalty
        #     and support hours."""

        #     results = self.store.similarity_search_with_score(
        #         query=question,
        #         k=self.settings.top_k,
        #     )

        #     if not results:
        #         return "Nothing found.", []

        #     texts = []
        #     sources = []

        #     for doc, score in results:
        #         texts.append(doc.page_content)

        #         sources.append({
        #             "sources": doc.metadata.get("sources"),
        #             "page": doc.metadata.get("page"),
        #             "score": round(score, 4),
        #         })

        #     combined_text = "\n\n".join(texts)
        #     return combined_text, sources

        self.agent = create_agent(
            model=get_chat_model(settings=self.settings),
            tools=[file_search(store=self.store, top_k=self.settings.top_k)],
            system_prompt=get_prompt(
                name="support/system",
                version=self.settings.system_prompt_version,
            ),
            middleware=default_stack(self.settings),
            
        )

    def ask(self, question: str) -> str:
        result = self.agent.invoke({
            "messages": [HumanMessage(content=question)]
        })

        messages = result["messages"]
        return messages[-1].text

    def close(self) -> None:
        if hasattr(self, "store") and self.store is not None:
            self.store.client.close()

