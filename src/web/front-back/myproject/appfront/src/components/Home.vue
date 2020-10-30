```vue
<template>
<div class="Home">
<el-row>
<el-table :data="userList" style="width: 100%" border>
<el-table-column prop="id" label="编号" min-width="100">
<template slot-scope="scope"> {{ scope.row.pk }} </template>
</el-table-column>
<el-table-column prop="name" label="用户名" min-width="100">
<template slot-scope="scope"> {{ scope.row.fields.name }} </template>
</el-table-column>
<el-table-column prop="email" label="邮箱" min-width="100">
<template slot-scope="scope"> {{ scope.row.fields.email }} </template>
</el-table-column>
<el-table-column prop="phone" label="电话" min-width="100">
<template slot-scope="scope"> {{ scope.row.fields.phone }} </template>
</el-table-column>
</el-table>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      input: '',
      userList: []
    }
  },
  mounted: function () {
    this.showUsers()
  },
  methods: {
    showUsers () {
      this.$http.get('http://127.0.0.1:8000/api/show_user')
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
            this.userList = res['list']
          } else {
            this.$message.error('查询用户列表失败')
            console.log(res['msg'])
          }
        })
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }
  ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

```
