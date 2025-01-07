#!/usr/bin/env python3
import logging
import sys
import time

import spear.client as client
import spear.transform.chat as chat
import spear.utils.io as io

from spear.proto.tool import BuiltinToolID
from spear.utils.tool import register_internal_tool

logging.basicConfig(
    level=logging.DEBUG,  # Set the desired logging level
    # Customize the log format
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(stream=sys.stderr)],  # Log to stderr
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

agent = client.HostAgent()


def handle(params):
    """
    handle the request
    """
    logger.info("Handling request: %s", params)

    logger.info("testing chat")
    test_chat("gpt-4o")

    logger.info("testing speak")
    test_speak("tts-1")

    logger.info("testing record")
    test_record("whisper-1")

    logger.info("testing input")
    test_input()

    logger.info("testing tool")
    test_tool()
    # test("text-embedding-ada-002")
    # test("bge-large-en-v1.5")

    time.sleep(10)
    # agent.stop()


def test_chat(model):
    """
    test the model
    """
    logger.info("Testing model: %s", model)

    resp = chat.chat(agent, "hi", model=model)
    logger.info(resp)
    resp = chat.chat(agent, "what is the time now?",
                     model=model, builtin_tools=[
                         BuiltinToolID.BuiltinToolID.Datetime,
                     ])
    logger.info(resp)


def test_speak(model):
    """
    test the model
    """
    logger.info("Testing model: %s", model)

    resp = io.speak(agent, "test test test")
    assert resp is not None


def test_record(model):
    """
    test the model
    """
    logger.info("Testing model: %s", model)

    resp = io.record(agent, "recording test")
    assert resp is not None


def test_input():
    """
    test the model
    """
    logger.info("Testing input")

    resp = io.input(agent, "input", True)
    logger.info(resp)


def test_tool_cb(param1, param2):
    """
    spear tool callback test function
    
    @param param1: test parameter 1
    @param param2: test parameter 2
    """
    logger.info("Testing tool callback %s %s", param1, param2)
    return "test"


def test_tool():
    """
    test the model
    """
    logger.info("Testing tool")
    tid = register_internal_tool(agent, test_tool_cb)
    logger.info("Registered tool: %d", tid)


if __name__ == "__main__":
    agent.register_handler("handle", handle)
    agent.run()
