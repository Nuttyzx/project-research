<template>
    <div class="hero min-h-px-16 py-28 justify-items-center mt-12 ">
        <div class="hero-content flex-col lg:flex-row-reverse">
            <!-- <div class="text-center lg:text-left px-12">
                <img :src="background" alt="Images login" />
            </div> -->
            
            <div class="card shrink-0 w-full max-w-sm shadow-2xl bg-base-100" style="width: 400px; "><br>
                <p class="text-3xl text-center text-black">เข้าสู่ระบบ</p>
                <form class="card-body " @submit.prevent="login">
                    <div class="form-control">
                        <label class="label">
                            <span class="label-text">อีเมล</span>
                        </label>
                        <input type="email" placeholder="salakorn@gmail.com" class="input input-bordered" v-model="username" required  />
                    </div>
                    <div class="form-control">
                        <label class="label">
                            <span class="label-text">รหัสผ่าน</span>
                        </label>
                        <input type="password" placeholder="********" class="input input-bordered" v-model="password"  required />
                        <!-- <label class="label">
                            <a href="#" class="label-text-alt link link-hover">หากลืมรหัสผ่าน?</a>
                        </label> -->
                    </div>
                    <div v-if="error" style="color: red;">{{ error }}</div>
                    <div class="form-control mt-6 ">
                        <button type="submit" class="btn btn-warning">เข้าสู่ระบบ</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
<script setup>
import { ref } from 'vue';
import background from "@/assets/images/research.jpg";
import router from "../../router";
import { useStore } from "vuex";

const username = ref('');
const password = ref('');
const error = ref('');
const store = useStore(); // เรียกใช้ store

const login = () => {
    // ตรวจสอบว่า username และ password ถูกต้องหรือไม่
    let isLogin = false;
    if (username.value === '' && password.value === ''){
        error.value = 'กรุณากรอกอีเมลและรหัสผ่านให้ครบถ้วนถูกต้อง';
        
    } else if (username.value === 'admin@gmail.com' && password.value === ''){
        error.value = 'ยังไม่ได้กรอกรหัสผ่าน กรุณากรอกรอกรหัสผ่านให้ถูกต้อง';
    } else if (username.value === '' && password.value === '12345678'){
        error.value = 'ยังไม่ได้กรอกอีเมล กรุณากรอกรอกอีเมลให้ถูกต้อง';
    } else if (username.value === 'admin@gmail.com' && password.value === '12345678') {
        isLogin = true;
        console.log("เข้าสู่ระบบ")
        alert('เข้าสู่ระบบสำเร็จ!');
        router.push({ name: "showuser" });
    } else {
        error.value = 'อีเมลหรือรหัสผ่านไม่ถูกต้อง กรุณากรอกอีเมลหรือรหัสผ่านใหม่อีกครั้ง';
        console.log(error.value);
    }
    store.commit("setLogin_status", isLogin); 
}
</script>



<!-- <template>
    <div class="hero min-h-px-16 py-11 ">
        <div class="hero-content flex-col lg:flex-row-reverse">
            <div class="text-center lg:text-left px-12">
                <img :src="background" alt="Images login" />
            </div>
            
            <div class="card shrink-0 w-full max-w-sm shadow-2xl bg-base-100"><br>
                <p class="text-4xl text-center">ลงชื่อเข้าใช้ แอดมิน</p>
                <form class="card-body">
                    <div class="form-control">
                        <label class="label">
                            <span class="label-text">อีเมล</span>
                        </label>
                        <input type="email" placeholder="salakorn@gmail.com" class="input input-bordered" v-model="username" required  />
                    </div>
                    <div class="form-control">
                        <label class="label">
                            <span class="label-text">รหัสผ่าน</span>
                        </label>
                        <input type="password" placeholder="********" class="input input-bordered" v-model="password"  required />
                        <!-- <label class="label">
                            <a href="#" class="label-text-alt link link-hover">หากลืมรหัสผ่าน?</a>
                        </label> -->
                    <!-- </div>
                    <div v-if="error" style="color: red;">{{ error }}</div>
                    <div class="form-control mt-6 ">
                        <button v-on:click="login" class="btn btn-warning">Login</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
<script >
import background from "@/assets/images/research.jpg";
import router from "../../router";
import { useStore } from "vuex";
const store = useStore(); // เรียกใช้ store

export default {
    data() {
        return {
            username: '',
            password: '',
            error: '',
            isLogin: false
        };
    },
    methods: {
        login(event) {
            event.preventDefault(); //ป้องกันการโหลดหน้าใหม่เมื่อกดปุ่ม "Login"
            // ตรวจสอบว่า username และ password ถูกต้องหรือไม่
            if(this.username === '' && this.password === ''){
                isLogin = false;
                this.error = 'กรุณากรอกอีเมลและรหัสผ่านให้ครบถ้วนถูกต้อง'
            }
            else if (this.username === 'admin@gmail.com' && this.password === ''){
                isLogin = false;
                this.error = 'ยังไม่ได้กรอกรหัสผ่าน กรุณากรอกรอกรหัสผ่านให้ถูกต้อง';
            }
            else if (this.username === '' && this.password === '12345678'){
                isLogin = false;
                this.error = 'ยังไม่ได้กรอกอีเมล กรุณากรอกรอกอีเมลให้ถูกต้อง';
            }
            else if (this.username === 'admin@gmail.com' && this.password === '12345678') {
                isLogin = true;
                console.log("เข้าสู่ระบบ")
                alert('เข้าสู่ระบบสำเร็จ!');
                router.push({ name: "showuser" });

            } else {
                isLogin = false;
                this.error = 'อีเมลหรือรหัสผ่านไม่ถูกต้อง กรุณากรอกอีเมลหรือรหัสผ่านใหม่อีกครั้ง';
                console.log(this.error)
            }
            store.commit("setLogin", isLogin); 
        }
    },
    computed: {
        background() {
            return background;
        }
    }

}

</script>
<style scoped> -->

<style scoped>
/* body{
    background-color: bg-gradient-to-r from-sky-500 to-indigo-500;
} */
</style>

