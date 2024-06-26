import redis from "redis";
const client = redis.createClient();


client
	.on("error", (error) => {
		console.log(`Redis client not connected to the server: ${error.message}`);
	})
	.on("connect", () => {
		console.log("Redis client connected to the server");
	});

const field = "HolbertonSchool";
const values = {
	Portland: '50',
	Seattle: '80',
	'New York': '20',
	Bogota: '20',
	Cali: '40',
	Paris: '2'
};

for (const [key, value] of Object.entries(values)) {
	client.hset(field, key, value, (_, reply) => redis.print(`Reply: ${reply}`));
}
client.hgetall(field, (_, object) => console.log(object));
