import kue from 'kue';

const blackListedNum =['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
	const full = 100;
	job.progress(0, full);

	if (blackListedNum.includes(phoneNumber)) {
		done(Error(`phone number ${phoneNumber} is blacklisted`));
		return;
	}

	job.progress(50, full);
	console.log(
		`Sending notification to ${phoneNumber}, with message: ${message}`
	);
	done();
}

const queue = kue.createQueue();

queue.process("push_notification_code_2", 2, (job, done) => {
	const { phoneNumber, message } = job.data;
	sendNotification(phoneNumber, message, job, done);
});
