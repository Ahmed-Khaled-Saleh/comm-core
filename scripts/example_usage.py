from comm_core import (
    Node,
    Message,
    Network,
    FullMeshTopology,
    IdealProtocol,
    IdentityChannel,
    AnalyticalBackend,
)


# -------------------------
# Nodes
# -------------------------

agent_1 = Node("agent_1")
agent_2 = Node("agent_2")

nodes = [
    agent_1,
    agent_2,
]


# -------------------------
# Communication system
# -------------------------

network = Network(
    nodes=nodes,

    topology=FullMeshTopology(
        [agent.id for agent in nodes]
    ),

    protocol=IdealProtocol(),

    backend=AnalyticalBackend(
        IdentityChannel()
    ),
)


# -------------------------
# Agent 1 communicates
# -------------------------

message = Message(
    sender="agent_1",
    receiver="agent_2",

    payload={
        "latent": [0.1, 0.2, 0.3],
    },

    type="world_model_latent",

    size_bits=3 * 32,
)


network.send(message)


# -------------------------
# Execute communication
# -------------------------

results = network.step()


print(results[0].success)


# -------------------------
# Agent 2 receives
# -------------------------

received = network.receive("agent_2")

print(received[0].payload)