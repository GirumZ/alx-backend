import kue from "kue";
import { expect } from "chai";
import createPushNotificationsJobs from "./8-job";

const queue = kue.createQueue();

describe("createPushNotificationsJobs", () => {
	before(() => {
		queue.testMode.enter();
	});

	afterEach(() => {
		queue.testMode.clear();
	});

	after(() => {
		queue.testMode.exit();
	});

	it("Testing if string is passed insteade of array", () => {
		expect(() => {
			createPushNotificationsJobs("holberton", queue);
		}).to.throw("Jobs is not an array");
	});
	it("Testing if an object is passed insteade of array", () => {
                expect(() => {
                        createPushNotificationsJobs("{}", queue);
                }).to.throw("Jobs is not an array");
        });
	it("Testing if a  number is passed insteade of array", () => {
                expect(() => {
                        createPushNotificationsJobs(2023, queue);
                }).to.throw("Jobs is not an array");
        });
});
