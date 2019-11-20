Vue.component('tasks-list', {
    props: {
        tasks: {
            type: Array,
            required: true
        },
        remaining: {
            type: Number,
            required: true
        }
    },
    data: function() {
        return {
            newTask: null,
            error: null
        }
    },
    methods: {
        submitTask() {
            if (this.newTask) {
                this.$emit('submit-task', this.newTask);
                this.newTask = null;
                if (this.error) {
                    this.error = null;
                }
            }
            else {
                this.error = 'Please enter some text';
            }
        },
        deleteTask(task) {
            this.$emit('delete-task', task)

        }
    },
    template: `
        <div class="container mt-2">
            <p><strong>{{ remaining }}</strong> elements in list</p>
            <div class="mt-2">
                <task-description
                    v-for="(task, index) in tasks"
                    :task="task"
                    :key="index"
                    @delete-task="deleteTask"
                ></task-description>

                <hr>
                <h3 class="text-danger">{{ error }}</h3>

                <form @submit.prevent="submitTask" class="mb-3">
                    <div class="form-group">
                    <input class="form-control"
                        id="taskDescription"
                        type="text"
                        v-model="newTask">
                    </div>
                    <button type="submit">Submit</button>
                </form>
            </div>
        </div>
    `
})

Vue.component('task-description', {
    props: {
        task: {
            type: String,
            required: true
        }
    },
    // methods: {
    //     deleteTask() {
    //         this.$emit('delete-task', this.task);
    //     }
    // },
    template: `
        <div class="alert alert-success">
            {{ this.task }}
            <button type="button" class="close" @click="deleteTask">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>
    `
})

var app = new Vue({
    el: '#app',
    data: {
        tasks: ['item one', 'item two']
    },
    computed: {
        tasksCount() {
            return this.tasks.length;
        }
    },
    methods: {
        addTask(task) {
            this.tasks.push(task);
        },
        removeTask(task) {
            this.tasks = this.tasks.filter(val => val !== task);
        }
    }
})
