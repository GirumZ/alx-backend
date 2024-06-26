import express from 'express';
import { createClient } from 'redis';
import { createQueue } from 'kue';
import { promisify } from 'util';

const app = express();
const client = createClient({ name: 'reserve_seat' });
const queue = createQueue();
const initialSeatCount = 50;
let reservationEnabled = false;
const port = 1245;

const reserveSeat = async (number) => {
	return promisify(client.set).bind(client)('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
	return promisify(client.get).bind(client)('available_seats');
};

app.get('/available_seats', (_, res) => {
	getCurrentAvailableSeats()
		.then((numberOfAvailableSeats) => {
			res.json({ numberofAvailableSeats })
		});
});

app.get('/reserve_seat', (_req, res) => {
	if(!reservationEnabled) {
		res.json({ status: 'Reservation are blocked' });
		return;
	}
	try {
		const job = queue.create('reserve_seat');
		job.on('failed', (err) => {
			console.log(
				'Seat reservation job',
				job.id,
				'failed:',
				err.message,
			);
		});
		job.on('complete', () => {
			console.log(
				'Seat reservation job',
                                job.id,
                                'completed'
			);
		});
		job.save();
		res.json({ status: 'Reservation in process' });
	} catch {
		res.json({ status: 'Reservation failed' });
	}
});
