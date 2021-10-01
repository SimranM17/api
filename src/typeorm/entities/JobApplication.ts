import { IsNotEmpty, IsString } from 'class-validator';
import { Entity, Column, PrimaryGeneratedColumn, UpdateDateColumn, CreateDateColumn, ManyToOne } from 'typeorm';
import { Company } from './Company';
import { User } from './users/User';

@Entity()
export class JobApplication {
  @PrimaryGeneratedColumn('increment')
  id: number;

  @Column()
  @IsString()
  role?: string;

  @Column()
  @IsString()
  description?: string;

  @Column()
  @IsNotEmpty()
  @ManyToOne(() => Company, (company: Company) => company.jobApplications)
  company: Company;

  @Column()
  @IsNotEmpty()
  @ManyToOne(() => User, (intern: User) => intern.jobApplications)
  internInformation: User;

  @Column()
  @IsString()
  status?: string;

  @Column()
  @IsString()
  appliedDate?: string;

  @Column()
  @CreateDateColumn()
  createdAt?: string = new Date().toISOString();

  @Column()
  @UpdateDateColumn()
  updatedAt?: string;

  public constructor(data?: JobApplication) {
    if (data) {
      this.role = data.role;
      this.description = data.description;
      this.company = data.company;
      this.internInformation = data.internInformation;
      this.status = data.status;
      this.appliedDate = data.appliedDate;
      this.updatedAt = new Date().toISOString();
    }
  }
}
