/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState, onMounted, onWillUnmount, onWillUpdateProps } from "@odoo/owl";

export class CountdownWidget extends Component {
    setup() {
        // Initialize countdown state and check if a countdown is already set
        this.state = useState({
            countdown: this.props.value || 10,
            isRunning: false,
            isPaused: false,
            isAlert: false,
            minutes: "00",
            seconds: "10",
            milliseconds: "0"
        });
        this.interval = null;

        // Update countdown display parts (minutes, seconds, milliseconds)
        this.updateCountdownParts();

        // Start countdown if it was running when mounted
        onMounted(() => {
            if (this.state.isRunning && !this.state.isPaused) {
                this.startCountdown();
            }
        });

        // Clear countdown interval when unmounting
        onWillUnmount(() => this.clearCountdown());

        // Sync with updates from form input
        onWillUpdateProps((nextProps) => {
            if (nextProps.value !== this.state.countdown) {
                this.state.countdown = nextProps.value;
                this.updateCountdownParts();
                if (this.state.isRunning) {
                    this.clearCountdown();
                    this.startCountdown();
                }
            }
        });
    }

    startCountdown() {
        if (this.state.isRunning) return;

        this.state.isRunning = true;
        this.state.isPaused = false;

        // Set countdown interval
        this.interval = setInterval(async () => {
            if (this.state.countdown > 0) {
                this.state.countdown = parseFloat((this.state.countdown - 0.05).toFixed(2));
                this.updateCountdownParts();

                // Enable alert mode when countdown is <= 4 seconds
                this.state.isAlert = this.state.countdown <= 4;

                // Update the record field with the current countdown
                await this.updateRecordCountdown(this.state.countdown);
            } else {
                this.clearCountdown();
                this.state.isRunning = false;
            }
        }, 50); // Update every 50ms for smoother rendering
    }

    updateCountdownParts() {
        const totalSeconds = Math.floor(this.state.countdown);
        const minutes = String(Math.floor(totalSeconds / 60)).padStart(2, "0");
        const seconds = String(totalSeconds % 60).padStart(2, "0");
        const milliseconds = String(Math.floor((this.state.countdown % 1) * 10));

        this.state.minutes = minutes;
        this.state.seconds = seconds;
        this.state.milliseconds = milliseconds;
    }

    pauseCountdown() {
        if (this.state.isPaused) {
            this.startCountdown();
        } else {
            this.clearCountdown();
        }
        this.state.isPaused = !this.state.isPaused;
    }

    stopCountdown() {
        this.clearCountdown();
        this.state.countdown = this.props.value || 10;
        this.updateCountdownParts();
        this.state.isRunning = false;
        this.state.isPaused = false;
        this.state.isAlert = false;
    }

    async updateRecordCountdown(value) {
        await this.props.record.update({ [this.props.name]: value });
    }

    clearCountdown() {
        if (this.interval) {
            clearInterval(this.interval);
            this.interval = null;
        }
    }
}

CountdownWidget.template = "dudoxx_automation.CountdownWidget";

registry.category("fields").add("countdown_widget", CountdownWidget);

console.log("CountdownWidget registered in the registry.");
