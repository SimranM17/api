import { Entity, Column, Index, PrimaryGeneratedColumn, OneToMany } from 'typeorm';
import { IsUrl, IsString, IsNumberString, IsNotEmpty } from 'class-validator';
import { JobApplication } from './JobApplication';

@Entity()
export class Company {
  @PrimaryGeneratedColumn('increment')
  id: number;

  @Column()
  @IsString()
  @IsNotEmpty()
  @Index({ unique: true })
  name: string;

  @Column()
  @IsNotEmpty()
  description: string;

  @Column()
  @IsUrl()
  logo?: string;

  @Column()
  @IsUrl()
  website?: string;

  @Column()
  @IsString()
  industry?: string;

  @Column()
  @IsNumberString()
  foundedYear?: string;

  @OneToMany(() => JobApplication, (jobApplication: JobApplication) => jobApplication.company)
  jobApplications: JobApplication[];

  public constructor(data?: Company) {
    if (data) {
      this.name = data.name;
      this.description = data.description;
      this.logo = data.logo;
      this.website = data.website;
      this.industry = data.industry;
      this.foundedYear = data.foundedYear;
    }
  }
}
